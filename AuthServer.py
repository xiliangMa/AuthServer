# -*- coding: utf-8 -*-

__author__ = 'xiliangma'

from backend.restApi.Resource import app


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)
