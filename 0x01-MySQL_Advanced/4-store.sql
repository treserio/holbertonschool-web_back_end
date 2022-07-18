-- create an insert trigger on orders
-- to remove associated quantity from items

CREATE TRIGGER rm_items
AFTER INSERT ON orders FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
