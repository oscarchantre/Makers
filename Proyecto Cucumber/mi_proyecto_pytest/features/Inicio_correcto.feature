
Feature: Inicio de sesion exitoso.

Scenario: El usuario  accede de manera correcta
    Given El usuario ingresa a https://www.saucedemo.com/
    When ingresa su username y password 
    And clic en login
    Then Inicia de sesión de manera correcta


