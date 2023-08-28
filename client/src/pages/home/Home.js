import React from "react";
import { useEffect } from "react";
import { $api } from "../../http/index";

export const Home = () => {
  const getUser = async () => {
    try {
      await $api.get("/api/user");
    } catch (e) {
      console.log(e.response.data.message);
    }
  };
  useEffect(() => {
    getUser();
  });

  return <div>Home</div>;
};
