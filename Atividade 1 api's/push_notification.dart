// Api do Firebase Cloud Messaging, mensagens são enviadas para a api e como "resposta" é enviada a notificação a todos os usuários da apliacação baseado na mensagem inserida.

//DATA='{"notification": {"body": "this is a body","title": "this is a title"}, "priority": "high", "data": {"click_action": "FLUTTER_NOTIFICATION_CLICK", "id": "1", "status": "done"}, "to": "<FCM TOKEN>"}'
//curl https://fcm.googleapis.com/fcm/send -H "Content-Type:application/json" -X POST -d "$DATA" -H "Authorization: key=<FCM SERVER KEY>"
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart';

class Messaging {

  static Client client = Client();

  static const String serverKey = 'AAAAGf1XLFg:APA91bGHcPNQPZQdBCi3Q3OiY0RxAVn5eEYCo5WRbfGOUVBWuY47mjy6-Zcv1I-YeAh3PRnmqY0Dc2d1VwSwGHDLEjEd0C_iC9qVj3ycEBh7G3UTGCFXWHnE2PE3VywIsIhUjWx5gz7S';
  static Future<Response> sendToAll({
    @required String text,
    @required String data,
    @required String fcmToken,
  }) =>
    client.post(
      'https://fcm.googleapis.com/fcm/send',
      body: json.encode({
        'notification': {'body': '$data','title': '$text'},
        'priority': 'high',
        'data': {
          'click_action':'FLUTTER_NOTIFICATION_CLICK',
          'id': '1',
          'status':'done'
        },
        'to': '$fcmToken',
      }),
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'key=$serverKey',
        },
    );
}
