import "./globals.css";
import Navbar from "./components/navbar";
import Header from "./components/header";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <Navbar />
        <main>{children}</main>
      </body>
    </html>
  );
}
