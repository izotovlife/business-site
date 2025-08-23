import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ServiceListPage from "./pages/ServiceListPage";
import ContactsPage from "./pages/ContactsPage";
import "./theme.css";

export default function App(){
  return (
    <BrowserRouter>
      <Header/>
      <main>
        <Routes>
<<<<<<< HEAD
          <Route index element={<Home />} />
          <Route path="services" element={<ServiceListPage />} />
          <Route path="contacts" element={<ContactsPage />} />
=======
          <Route path="/" element={<Home/>}/>
          <Route path="/services" element={<ServiceListPage/>}/>
          <Route path="/contacts" element={<ContactsPage/>}/>
>>>>>>> origin/main
          <Route path="*" element={<div className="container">Страница не найдена</div>} />
        </Routes>
      </main>
      <Footer/>
    </BrowserRouter>
  );
}
