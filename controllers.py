from flask import jsonify

def get_pending_messages(supabase):
    response = supabase.table('messages').select('*').eq('approved', False).execute()
    return jsonify(response.data)

def approve_message(supabase, message_id):
    response = supabase.table('messages').update({'approved': True}).eq('id', message_id).execute()
    return jsonify({'success': True, 'data': response.data})

def reject_message(supabase, message_id):
    response = supabase.table('messages').delete().eq('id', message_id).execute()
    return jsonify({'success': True, 'data': response.data})

def get_approved_messages(supabase):
    response = supabase.table('messages').select('*').eq('approved', True).execute()
    return jsonify(response.data)

def add_message(supabase, data):
    response = supabase.table('messages').insert({
        'username': data['username'],
        'content': data['message'],
        'approved': False
    }).execute()
    return jsonify({'success': True, 'data': response.data})