-- 코드를 입력하세요
SELECT DISTINCT cart_id FROM cart_products 
WHERE cart_id IN (
    SELECT cart_id FROM cart_products WHERE name = 'Milk'
) AND cart_id IN (
    SELECT cart_id FROM cart_products WHERE name = 'Yogurt'
);