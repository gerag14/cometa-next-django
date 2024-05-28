import Link from "next/link";

interface OrderCardDetailProps {
  items: {
    uuid: string;
    product_name: string;
    quantity: number;
    price: string;
  }[];
}

const OrderCard: React.FC<OrderCardDetailProps> = ({ items }) => {
  return (
    <div className="mt-2">
      <ul>
        {items.map((item) => (
          <li key={item.uuid} className="border p-2 mb-2 rounded">
            <div className="font-bold text-lg">Item: {item.product_name}</div>
            <div className="text-sm">Quantity: {item.quantity}</div>
            <div className="text-sm">Price: ${item.price}</div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default OrderCard;
