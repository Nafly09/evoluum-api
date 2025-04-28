from fastapi.responses import JSONResponse


class Exceptions:
    @staticmethod
    def handler_error_404():
        return JSONResponse(status_code=404, content={"msg": "Not Found"})

    @staticmethod
    def handler_error_500():
        return JSONResponse(status_code=500, content={"msg": "Internal Error"})

    @staticmethod
    def handler_error_400():
        return JSONResponse(status_code=400, content={"msg": "Bad Request"})