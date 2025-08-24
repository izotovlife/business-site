// frontend/src/components/Footer.js
import React from "react";
import { useOrderModal } from "../OrderModalContext";
import "./Footer.css";

export default function Footer() {
  const { open } = useOrderModal();

  return (
    <footer className="site-footer">
      <div className="container footer-row">
        <div className="copyright">© {new Date().getFullYear()} IZOTOVLIFE</div>
        <button className="btn" onClick={open}>Оставить заявку</button>
      </div>
    </footer>
  );
}
