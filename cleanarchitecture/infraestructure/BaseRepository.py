class BaseRepository:
    conn:str
    
    @staticmethod
    def setConnectionString(value:str) -> None:
        BaseRepository.conn = value
        print(BaseRepository.conn)