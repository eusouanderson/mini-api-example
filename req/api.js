const { fetchProdutos, fetchEmpresas } = require('./index.js');


const produtos = fetchProdutos();
//const empresas = fetchEmpresas();


console.log(produtos);
