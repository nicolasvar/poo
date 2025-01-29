import logging
from fastapi import FastAPI
import uvicorn

from controllers.UserController import UserController


class Program:
    app: FastAPI 
    logger: logging.Logger

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing program")
        self.app = FastAPI(
            title="Mi primera API",
            description="Esta es prueba",
            docs_url="/swagger",
        )
        UserController(self.app)

    def main(self) -> None:
        uvicorn.run("Program:program.app", host="0.0.0.0", port=8000, reload=True)
        
program = Program()
if __name__ == "__main__":
    program.main()