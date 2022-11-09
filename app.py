# Importing
from flask import Flask, render_template, request

# Importing custom libs
from lib.rsa import RSA

# Env setup
app = Flask(__name__)

# Mini helper
def get_missing_data(data_arr, expected_arr):
    missing = []
    for expected_item in expected_arr:
        if expected_item not in data_arr:
            missing.append(f"Oops, {expected_item} seems to be missing.")
    
    return missing

def get_clear_data():
    rsa = RSA()
    data = {}
    data['prime_p'] = rsa.primes['p']
    data['prime_q'] = rsa.primes['q']
    data['public_key_n'] = rsa.public_key[0]
    data['public_key_e'] = rsa.public_key[1]
    data['private_key_n'] = rsa.private_key[0]
    data['private_key_d'] = rsa.private_key[1]

    return data


# Flask endpoints
@app.route('/', methods=["GET", "POST"])
def main_page():
    # GET REQUEST
    if request.method == 'GET':
        data = get_clear_data()
        return render_template("rsa.html", data = data)
    
    # POST REQUEST
    # Missing data handling
    print(request.form.keys())
    missing_data_errors = get_missing_data(request.form.keys(), ['action','prime_p', 'prime_q', 'public_key_n', 'public_key_e', 'private_key_n', 'private_key_d'])
    if missing_data_errors != []:
        data = get_clear_data()
        return render_template("rsa.html", data = data, errors = missing_data_errors)

    # Getting data
    action = request.form.get('action')
    prime_p = request.form.get('prime_p')
    prime_q = request.form.get('prime_q')

    public_key_n = request.form.get('public_key_n') 
    public_key_e = request.form.get('public_key_e') 
    private_key_n = request.form.get('private_key_n') 
    private_key_d = request.form.get('private_key_d')
    # Should check if public and private n are equal

    # TODO: Should check if inputs are really valid numbers
    public_key = (int(public_key_n), int(public_key_e))
    private_key = (int(private_key_n), int(private_key_d))

    # Format data output
    data = {}
    data['prime_p'] = prime_p
    data['prime_q'] = prime_q
    data['public_key_n'] = public_key_n
    data['public_key_e'] = public_key_e
    data['private_key_n'] = private_key_n
    data['private_key_d'] = private_key_d

    # Encrypting
    rsa = RSA()
    if action.lower() == 'encrypt':
        data['to_encrypt'] = request.form.get('to_encrypt')
        try:
            encrypted = rsa.encrypt(data['to_encrypt'], public_key)
        except Exception as e:
            data = get_clear_data()
            return render_template("rsa.html", data = data, errors = ['Oops, something went wrong while encrypting. Try again!'])
        data['encrypted'] = encrypted

    # Decrypting
    elif action.lower() == 'decrypt':
        data['to_encrypt'] = request.form.get('to_encrypt')
        data['encrypted'] = request.form.get('to_decrypt')
        try:
            decrypted = rsa.decrypt(data['encrypted'], private_key)
        except Exception as e:
            data = get_clear_data()
            return render_template("rsa.html", data = data, errors = ['Oops, something went wrong while decrypting. Try again!'])
        data['decrypted'] = decrypted

    return render_template('rsa.html', data=data)

if __name__ == "__main__":
    app.run()