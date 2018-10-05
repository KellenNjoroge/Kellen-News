from flask import render_template
from . import main


@main.app_errorhandler(404)
def four_Ow_four(error):

    """
     function to render the 404 error page
     :param error:
     """
    return render_template('404.html'), 404
