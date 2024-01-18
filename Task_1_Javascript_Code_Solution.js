// Steps to use the code
// 1 - Enter the quantity of products asked respectively in the prompt.
// 2 - Enter "yes" or "no" for gift wrapping in the prompt and press enter.
// Output will be shown in the console

// Make an object for the Products with Product Name and Price
const productList = {
    "A": 20,
    "B": 40,
    "C": 50
};

// Function for bulk_5_discount with the required condition
function bulk5Discount(quantityOfProducts) {
    const keyList = Object.keys(quantityOfProducts);
    const valList = Object.values(quantityOfProducts);
    const position = valList.indexOf(Math.max(...valList));
    const productTotalAmount = productList[keyList[position]] * Math.max(...valList);
    return productTotalAmount * (-0.05);
}

// Function for bulk_10_discount with the required condition
function bulk10Discount(productsTotalAmount) {
    return productsTotalAmount * (-0.1);
}

// Function for tiered_50_discount with the required condition and return the Product total amount
function tiered50Discount(quantityOfProducts) {
    let totalDiscount = 0;
    for (const [key, value] of Object.entries(quantityOfProducts)) {
        if (value > 15) {
            totalDiscount += (value - 15) * productList[key] * 0.5;
        }
    }
    return totalDiscount * -1;
}

// Function applicableDiscounts and apply all the conditions to get the minimum amount and maximum discount
function applicableDiscounts(quantityOfProducts, productTotalQuantity, productsTotalAmount) {
    const discounts = [];

    if (productsTotalAmount > 200) {
        discounts.push(["flat_10_discount", -10]);
    }

    if (Math.max(...Object.values(quantityOfProducts)) > 10) {
        discounts.push(["bulk_5_discount", bulk5Discount(quantityOfProducts)]);
    }

    if (productTotalQuantity > 20) {
        discounts.push(["bulk_10_discount", bulk10Discount(productsTotalAmount)]);
    }

    if (productTotalQuantity > 30 && Math.max(...Object.values(quantityOfProducts)) > 15) {
        discounts.push(["tiered_50_discount", tiered50Discount(quantityOfProducts)]);
    }

    return discounts;
}

// Function bestDiscount for getting the best discount and maximum discount
function bestDiscount(discountsApplicable) {
    if (discountsApplicable.length === 0) {
        return ["No Discount", 0];
    }

    let bestDiscount = "";
    let bestAmount = 0;

    for (const [discount, amount] of discountsApplicable) {
        if (Math.abs(bestAmount) < Math.abs(amount)) {
            bestAmount = amount;
            bestDiscount = discount;
        }
    }

    return [bestDiscount, bestAmount];
}

// Function totalAmount for multiplying quantityOfProduct and productList
function totalAmount(quantityOfProducts) {
    let total = 0;
    for (const [key, value] of Object.entries(quantityOfProducts)) {
        total += value * productList[key];
    }
    return total;
}

// Function for gift wrap fee is $1 per unit.
function giftWrapFee(productTotalQuantity) {
    return productTotalQuantity * 1;
}

// Function for Shipping fee, 10 units can be packed in one package,
// and the shipping fee for each package is $5.
function shippingFee(productTotalQuantity) {
    return productTotalQuantity % 10 === 0 ? (productTotalQuantity / 10) * 5 : Math.ceil(productTotalQuantity / 10) * 5;
}

// Function cart which contains all the details about the Products and billing
function cart(quantityOfProducts, giftWrap) {
    const productTotalQuantity = Object.values(quantityOfProducts).reduce((acc, val) => acc + val, 0);
    const productsTotalAmount = totalAmount(quantityOfProducts);
    const discountsApplicable = applicableDiscounts(quantityOfProducts, productTotalQuantity, productsTotalAmount);
    const [topDiscount, discountAmount] = bestDiscount(discountsApplicable);
    let feeGiftWrap = 0;

    if (giftWrap === "yes") {
        feeGiftWrap = giftWrapFee(productTotalQuantity);
    }

    const shippingCharge = shippingFee(productTotalQuantity);
    const grandTotal = productsTotalAmount + discountAmount + shippingCharge + feeGiftWrap;

    return [productsTotalAmount, topDiscount, discountAmount, feeGiftWrap, shippingCharge, grandTotal];
}

// Function to get user input for product quantities
function getUserInputForQuantities() {
    const quantities = {};
    const products = Object.keys(productList);

    for (const product of products) {
        const quantity = prompt(`Enter quantity of Product ${product}: `);
        quantities[product] = parseInt(quantity, 10) || 0;
    }

    return quantities;
}

// Function to get user input for gift wrapping
function getUserInputForGiftWrap() {
    const response = prompt(`Do you want gift wrapping? (yes/no): `).toLowerCase();
    return response === 'yes' ? 'yes' : 'no';
}

// Sample usage with user input
const quantityOfProducts = getUserInputForQuantities();
const giftWrap = getUserInputForGiftWrap();

console.log("\n************************** cart details **********************************\n");

const [subtotal, topDiscount, discountAmount, feeGiftWrap, shippingCharge, grandTotal] = cart(quantityOfProducts, giftWrap);

console.log("Product Name\tQuantity\tAmount");
for (const [key, value] of Object.entries(quantityOfProducts)) {
    const productAmount = value * productList[key];
    console.log(`${key}\t\t${value}\t\t${productAmount}`);
}

console.log(`\nSubtotal\t\t${subtotal}`);
console.log(`${topDiscount}\t\t${discountAmount}`);
console.log(`Shipping Charge\t\t${shippingCharge}`);
console.log(`Gift Wrap Fee\t\t${feeGiftWrap}\n`);
console.log(`Grand Total\t\t${grandTotal}`);
