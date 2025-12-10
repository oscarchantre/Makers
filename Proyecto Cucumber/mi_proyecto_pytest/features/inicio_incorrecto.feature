Feature: Inicio de sesion incorrecto.

Scenario: El usuario  no accede a la plataforma
    Given El usuario ingresa a https://www.saucedemo.com/
    When ingresa su username y password incorrecto
    And clic en login
    Then El sistema muestra una alerta de error
