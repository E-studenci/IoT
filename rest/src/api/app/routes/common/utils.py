from api.app.response_parser import ResponseData, response_wrapper, ResponseError
from api.utils.card import LAST_SCANNED_CARD
from flask_login import login_required
from flask import request
from api import APP
import datetime

UTILS_ROUTE = "/utils"

@APP.route(UTILS_ROUTE + "/get_scanned_card", methods=['GET'])
@login_required
@response_wrapper()
def get_scanned_card():
    result = LAST_SCANNED_CARD
    if result.scanned is None:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="no scanned card in last 3 minutes")
        )
    since_last_scan = (datetime.datetime.now() - result.scanned).total_seconds()/60
    if result.scanned is None or since_last_scan > 3:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="no scanned card in last 3 minutes")
        )
    return ResponseData(
        code = 200,
        data={"rfid": result.rfid}
    )