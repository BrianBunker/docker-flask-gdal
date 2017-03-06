import geo
from os import path

from flask import Flask
from flask import request
from flask import send_file


app = Flask(__name__)


@app.route("/")
def root():
    # Parse querystring params
    index = request.args.get("index")

    if not isinstance(index, basestring):
        return help_message

    # Dynamically determine the index function to use
    func = index_funcs.get(index.lower())

    # Make sure the index function requested is available
    if not callable(func):
        return help_message

    # Calculate the index and send it as the response
    image_fname = func()
    return send_file(image_fname, mimetype="image/tiff",
                     as_attachment=True,
                     attachment_filename=path.basename(image_fname))

index_funcs = {
    "vari": geo.vari,
    "ndvi": geo.ndvi,
    "rdvi": geo.rdvi
}

help_message = "Use <pre>?index=&ltindex&gt</pre> to specify a vegetation " \
               "index for the image. Available indexes: " \
               "<pre>{list_of_indexes}</pre>".format(
                    list_of_indexes=",".join(index_funcs.keys())
                )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
