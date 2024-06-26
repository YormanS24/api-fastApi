from category.schema.CategorySchema import CategoryRequest;
from category.models.Category import Category;
from config.DataBase import SessionLocal;

class CategoryService:
    
    def createCategory(request: CategoryRequest) -> dict:
        db = SessionLocal();
        existCategory = db.query(Category).filter(Category.name == request.name).first();
        
        if existCategory:
            return {"message":"ya se encuentra una categoria registrada con el nombre de: "+request.name},{"status_code":409};
            
        db.add(Category(**request.model_dump()));
        db.commit();
        db.close();
        return {"message":"categoria registrada con exito"},{"status_code":201};
    
    def getCategoryById(id:int) -> dict:
        db = SessionLocal();
        existCategory = db.query(Category).filter(Category.categoryId == id).first();
        
        if not existCategory:
            return {"message":"no esta disponible la categoria"},{"status_code":404};

        return {"message":existCategory},{"status_code":200};

    
    def updateCategory(id:int,request:CategoryRequest) -> dict:
        db = SessionLocal();
        existCategory = db.query(Category).filter(Category.categoryId == id).first();
        
        if not existCategory:
            return {"message":"no esta disponible la categoria"},{"status_code":404};
        
        existCategory.name = request.name;
        existCategory.description = request.description;
        
        db.commit();
        db.close();
        
        return {"message":"actualiozacion con exito"},{"status_code":200};
    
    def deleteCategory(id: int) -> dict:
        db = SessionLocal();
        existCategory = db.query(Category).filter(Category.categoryId == id).first();
        
        if not existCategory:
            return {"message":"no esta disponible la categoria"},{"status_code":404};
        
        db.delete(existCategory);
        db.commit();
        
        return {"message":"categoria eliminada con exito"},{"status_code":200};