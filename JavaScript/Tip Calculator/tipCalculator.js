function calculateTip() {
    var billAmount = document.getElementById('billAmount').value;
    var tipPercentage = document.getElementById('tipPercentage').value;

    var tipAmount = billAmount * (tipPercentage / 100);
    var totalAmount = parseFloat(billAmount) + tipAmount;

    document.getElementById('totalAmount').innerHTML = 'Total Amount (including tip): $' + totalAmount.toFixed(2);
}
