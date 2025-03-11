document.addEventListener('DOMContentLoaded', () => {
    const tradeForm = document.getElementById('trade-form');
    if (tradeForm) {
        tradeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(tradeForm);
            const response = await fetch('/buy_stock', {
                method: 'POST',
                body: formData,
            });
            const result = await response.json();
            alert(result.message);
        });
    }
});