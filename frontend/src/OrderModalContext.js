import { createContext, useContext, useState } from "react";
import OrderModal from "./components/OrderModal";

const OrderModalContext = createContext(null);

export function OrderModalProvider({ children }) {
  const [state, setState] = useState({ open: false, preset: null, serviceId: null });

  const openModal = (preset = "site", serviceId = null) => {
    setState({ open: true, preset, serviceId });
  };

  const closeModal = () => setState((s) => ({ ...s, open: false }));

  return (
    <OrderModalContext.Provider value={{ openModal }}>
      {children}
      <OrderModal
        open={state.open}
        onClose={closeModal}
        preset={state.preset}
        serviceId={state.serviceId}
      />
    </OrderModalContext.Provider>
  );
}

export function useOrderModal() {
  const ctx = useContext(OrderModalContext);
  if (!ctx) throw new Error("useOrderModal must be used within OrderModalProvider");
  return ctx;
}

