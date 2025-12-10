Feature: validacion de campos.

Scenario: se valida los campos
    Given El usuario ingresa a https://www.saucedemo.com/
    When clic en login
    Then El sistema muestra una alerta de errores
