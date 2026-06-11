import json

from fastapi import APIRouter, Request

from services.receipt_service import ReceiptService

router = APIRouter(tags=["Webhook routes"])

receipt_service = ReceiptService()


@router.post("/messages-upsert")
async def webhook(request: Request):
    body = await request.body()
    data = json.loads(body.decode())

    message = data.get("data", {})
    message_id = message.get("key", {}).get("id")

    if not message_id:
        return {"error": "invalid message"}

    result = receipt_service.process_message(message_id)

    print(result)

    return {"status": "ok", "data": result}
