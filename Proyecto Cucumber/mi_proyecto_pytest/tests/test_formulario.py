import re
import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect
from datetime import datetime

# Ruta relativa al feature (ajusta si tu estructura difiere)
scenarios("../features/inicio_correcto.feature")
scenarios("../features/inicio_incorrecto.feature")
scenarios("../features/validacion_campos.feature")


@given('El usuario ingresa a https://www.saucedemo.com/')
def step_ingresar_web(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(3000)



@when('ingresa su username y password')
def step_diligenciar_formulario(page: Page):
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")


@when('clic en login')
def step_clic_login(page: Page):
    page.locator("[data-test=\"login-button\"]").click()


@then('Inicia de sesión de manera correcta')
def step_mensaje_resumen(page: Page):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path_timestamped = f"tests/evidencias/screenshot_login_{timestamp}.png"
    page.screenshot(path=screenshot_path_timestamped, full_page=True)


    #incorrecto login
    
@when('ingresa su username y password incorrecto')
def step_diligenciar_formulario(page: Page):
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce1")

@then('El sistema muestra una alerta de error')
def step_mensaje_error(page: Page):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path_timestamped = f"tests/evidencias/screenshot_login_Error_{timestamp}.png"
    page.screenshot(path=screenshot_path_timestamped, full_page=True)

    #validacion de campos

@then('El sistema muestra una alerta de errores')
def step_mensaje_errores(page: Page):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path_timestamped = f"tests/evidencias/screenshot_login_Vallidacion_campos_{timestamp}.png"
    page.screenshot(path=screenshot_path_timestamped, full_page=True)
