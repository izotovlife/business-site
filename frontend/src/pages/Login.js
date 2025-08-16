import React, { useState, useEffect } from "react";
import axios from "axios/dist/node/axios.cjs";
import "./Login.css";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default function Login(){
  const [form, setForm] = useState({username:"", password:""});
  const [error, setError] = useState("");

  useEffect(()=>{
    axios.get("/accounts/login/", {withCredentials:true}).catch(()=>{});
  },[]);

  const onChange = e => setForm({...form, [e.target.name]: e.target.value});

  const submit = e => {
    e.preventDefault();
    setError("");
    axios
      .post("/accounts/login/", form, { withCredentials: true })
      .then(() => axios.get("/admin-link/", { withCredentials: true }))
      .then((r) => {
        window.location.href = r.data.url;
      })
      .catch(() => setError("Неверные данные"));
  };

  return (
    <section className="container">
      <h1 className="section-title">Вход для сотрудников</h1>
      <form className="login-form" onSubmit={submit}>
        <input
          type="text"
          name="username"
          placeholder="Логин"
          value={form.username}
          onChange={onChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Пароль"
          value={form.password}
          onChange={onChange}
        />
        {error && <div className="error">{error}</div>}
        <button className="btn" type="submit">Войти</button>
      </form>
    </section>
  );
}
