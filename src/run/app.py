import streamlit as st
import pandas as pd
from objects.app import App
import threading


def app():
    start_app = App()
    start_app.executeApp()
    
if __name__ == "__main__":
    app()