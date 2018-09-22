describe('Generar paletas de colores', function() {
    it('Visita la pagina y genera dos paletas', function() {
	      //acceder a la pagina de la aplicacion
        cy.visit('https://adbetin.github.io/miso4208-s7-testapp/palette.html')
        cy.get('button').first().click()
        cy.wait(2000)
        cy.screenshot(Cypress.env('registerid') + "-initial");

        cy.get('button').first().click()
        cy.wait(2000)
        cy.screenshot(Cypress.env('registerid') + "-final");
	})
})
