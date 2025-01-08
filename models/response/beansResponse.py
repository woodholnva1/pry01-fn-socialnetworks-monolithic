from flask import jsonify

# Clase para Responder Genericamente al API
class BeanResponse:
    MESSAGE_P = "Oops, something went wrong"

    def notfound(self, message, detail) -> jsonify:
        response = jsonify(
            {"message": self.MESSAGE_P if not detail else detail,
             "detail": message}
        )
        response.status_code = 404
        return response

    def notesperated(self, message: str, detail: str = None) -> jsonify:
        response = jsonify(
            {"detail": self.MESSAGE_P if not detail else detail,
             "message": message}
        )
        response.status_code = 500
        return response

    def success(self, message, detail:str = None) -> jsonify:
        response = jsonify(
            {"message": self.MESSAGE_P if not detail else detail,
             "detail": message}
        )
        response.status_code = 200
        return response
