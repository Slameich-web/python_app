import React from "react";
import Login from "./pages/login/Login";
import { Home } from "./pages/home/Home";
import { Routes, Route, Link } from "react-router-dom";
import "./App.scss";
import Register from "./pages/register/Register";

const App = () => {
  return (
    <>
      <Link to="/home">Home</Link>
      <Link to="/login">login</Link>
      <Link to="/register">register</Link>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </>
  );
};

export default App;
