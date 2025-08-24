// frontend/src/components/OrderModal.js
import React, { useEffect, useState, useCallback } from "react";
import api from "../Api";
import "./OrderModal.css";

export default function OrderModal({ open, onClose, preset }) {
  const [form, setForm] = useState({ name: "", contact: "", message: "" });
  const [status, setStatus] = useState(null); // null | "loading" | "ok" | "err"

  useEffect(() => {
    if (!open) return;
    const onKey = (e) => e.key === "Escape" && status !== "loading" && onClose();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, status, onClose]);

  const isValid = form.name.trim() && form.contact.trim();

  const submit = useCallback(
    async (e) => {
      e.preventDefault();
      if (!isValid || status === "loading") return;

      setStatus("loading");
      try {
        await api.post("/leads/", {
          name: form.name.trim(),
          contact: form.contact.trim(),
          message: form.message.trim(),
          source: preset || "site",
        });

        setStatus("ok");
        setForm({ name: "", contact: "", message: "" });
        setTimeout(() => onClose(), 900);
      } catch (err) {
        console.error("Lead submit failed:", err);
        setStatus("err");
      }
    },
    [form, isValid, preset, status, onClose]
  );

  if (!open) return null;

  const onBackdropClick = () => status !== "loading" && onClose();

  return (
    <div
      className="modal-backdrop"
      onClick={onBackdropClick}
      role="dialog"
      aria-modal="true"
      aria-labelledby="order-modal-title"
    >
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <button
          className="modal-close"
          onClick={onClose}
          aria-label="Закрыть"
          disabled={status === "loading"}
        >
          ×
        </button>

        <h3 id="order-modal-title">Оставить заявку</h3>

        <form onSubmit={submit} className="modal-form" noValidate>
          <input
            required
            placeholder="Ваше имя"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
          />

          <input
            required
            placeholder="Телефон, email или Telegram"
            value={form.contact}
            onChange={(e) => setForm({ ...form, contact: e.target.value })}
          />

          <textarea
            rows={4}
            placeholder="Кратко опишите задачу"
            value={form.message}
            onChange={(e) => setForm({ ...form, message: e.target.value })}
          />

          <button className="btn" type="submit" disabled={!isValid || status === "loading"}>
            {status === "loading" ? "Отправляем..." : "Отправить"}
          </button>

          {status === "ok"  && <div className="hint ok">Готово! Свяжемся с вами.</div>}
          {status === "err" && <div className="hint err">Ошибка при отправке. Попробуйте ещё раз.</div>}
        </form>
      </div>
    </div>
  );
}
