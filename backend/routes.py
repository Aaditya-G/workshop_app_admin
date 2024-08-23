from flask import jsonify, request
from controllers import (
    get_pending_messages,
    approve_message,
    reject_message,
    get_approved_messages,
    add_message
)

def configure_routes(app, supabase):
    @app.route('/api/pending-messages')
    def pending_messages():
        return get_pending_messages(supabase)

    @app.route('/api/approve-message', methods=['POST'])
    def approve():
        return approve_message(supabase, request.json['id'])

    @app.route('/api/reject-message', methods=['POST'])
    def reject():
        return reject_message(supabase, request.json['id'])

    @app.route('/api/approved-messages')
    def approved_messages():
        return get_approved_messages(supabase)

    @app.route('/add', methods=['POST'])
    def add():
        return add_message(supabase, request.json)