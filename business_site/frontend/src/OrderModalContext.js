// frontend/src/OrderModalContext.js
import React, { createContext, useContext, useState, useCallback } from "react";
import OrderModal from "./components/OrderModal";

const Ctx = createContext({ open: () => {}, close: () => {} });

export function OrderModalProvider({ children }) {
  const [isOpen, setIsOpen] = useState(false);
  const open = useCallback(() => setIsOpen(true), []);
  const close = useCallback(() => setIsOpen(false), []);

  return (
    <Ctx.Provider value={{ open, close }}>
      {children}
      {/* одна глобальная модалка на всё приложение */}
      <OrderModal open={isOpen} onClose={close} />
    </Ctx.Provider>
  );
}

export function useOrderModal() {
  return useContext(Ctx);
}
