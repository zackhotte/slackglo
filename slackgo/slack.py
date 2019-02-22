from flask import Blueprint, request, json

bp_slack = Blueprint('slack', __name__, url_prefix='/api/v1/slack')


@bp_slack.route('/challenge', methods=['POST'])
def challenge():
    data = json.loads(request.data)
    return json.jsonify({'challenge': data['challenge']})
