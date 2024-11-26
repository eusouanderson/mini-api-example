const axios = require('axios');

async function fetchProdutos() {
    try {
        const response = await axios.get('https://api.buscanarede.com.br/produtos', {
            headers: {
                'Authorization': 'Bearer AEDGE$GGFGAA$@565',
            },
            params: {
                empresa : '3'
            }
        });
        console.log(response.data);
    } catch (error) {
        console.error('Erro ao fazer a requisição:', error);
    }
}

async function fetchEmpresas() {
    try {
        const response = await axios.get('https://api.buscanarede.com.br/empresas', {
            headers: {
                'Authorization': 'Bearer AEDGE$GGFGAA$@565',
            }
        });
        console.log(response.data);
    } catch (error) {
        console.error('Erro ao fazer a requisição:', error);
    }
}


module.exports = {
    fetchProdutos,
    fetchEmpresas
};
