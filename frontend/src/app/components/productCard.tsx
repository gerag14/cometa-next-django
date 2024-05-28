"use client";

import Link from "next/link";

interface ProductCardProps {
  product: {
    uuid: string;
    name: string;
    description: string;
    stock: string;
  };
}

const ProductCard = ({ product }) => {
  return (
    <div className="border p-4 rounded shadow-md mb-4 max-w-[600px]">
      <div>Product: {product.name}</div>
      <div>Description: ${product.description}</div>
      <div>Stock: {product.stock}</div>
    </div>
  );
};

export default ProductCard;
