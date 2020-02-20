# coding: utf-8

from flask import Flask, request, Response, redirect, url_for, render_template, jsonify, make_response, send_file


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == '-D':
        app.run(host='0.0.0.0',debug=True)
    else:
        app.run()

