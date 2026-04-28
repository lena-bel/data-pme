import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

ventes_produit = données.groupby('produit')['qte'].sum().reset_index()

fig1 = px.bar(ventes_produit, x='produit', y='qte', title='...')
fig1.write_html('ventes-par-produit.html')

#create a new column for chiffre d'affaire
données['ca'] = données['prix'] * données['qte']
chiffre_affaire = données.groupby('produit')['ca'].sum().reset_index()
fig2 = px.bar(chiffre_affaire, x='produit', y='ca', title='Chiffre d\'affaires par produit')
fig2.write_html('chiffre-affaire.html')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
