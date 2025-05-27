const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

app.post('/calcular', (req, res) => {
    const { despesas, receita } = req.body;
    
    if (isNaN(despesas) || isNaN(receita)) {
        return res.status(400).json({ erro: 'Insira valores numéricos válidos!' });
    }

    const economia = receita - despesas;
    res.json({ economia: economia.toFixed(2) });
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});


