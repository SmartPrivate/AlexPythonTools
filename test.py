import model_generator

if __name__ == "__main__":
    host: str = 'localhost'
    port: int = 3306
    db_name = 'mysql'
    user = 'root'
    password = 'root'
    mg = model_generator.ModelGenerator(host=host, port=port, db_name=db_name, user=user, password=password)
