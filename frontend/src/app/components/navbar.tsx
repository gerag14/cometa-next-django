"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

const Navbar = () => {
  const pathname = usePathname();

  return (
    <>
      <div className="w-full h-20 bg-emerald-800 sticky top-0">
        <div className="container mx-auto px-4 h-full flex justify-center items-center">
          <nav>
            <ul className="flex space-x-4">
              <li>
                <Link
                  className={`link ${
                    pathname === "/customers" ? "active-link font-bold" : ""
                  }`}
                  href="/customers"
                >
                  Customers
                </Link>
              </li>
              <li>
                <Link
                  className={`link ${
                    pathname === "/products" ? "active-link font-bold" : ""
                  }`}
                  href="/products"
                >
                  Products
                </Link>
              </li>
              <li>
                <Link
                  className={`link ${
                    pathname === "/orders" ? "active-link font-bold" : ""
                  }`}
                  href="/orders"
                >
                  Orders
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </>
  );
};

export default Navbar;
