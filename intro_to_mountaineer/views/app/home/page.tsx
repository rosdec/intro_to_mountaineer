import React, { useState } from "react";
import { ServerState, useServer } from "./_server/useServer";

const CreatePost = ({ serverState }: { serverState: ServerState }) => {
  const [newBlogpost, setNewBlogpost] = useState("");

  return (
    <div>
      <input type="text"
        value={newBlogpost}
        onChange={(e) => setNewBlogpost(e.target.value)} />
      <button
        onClick={
          async () => {
            await serverState.add_blogpost({
              payload: newBlogpost.toString()
            });
            setNewBlogpost("");
          }}>

        Post</button>
    </div>
  );
};


const ShowPosts = ({ serverState }: { serverState: ServerState }) => {
  return (
    serverState.posts.map((post) => (
      <div key={post.id}>
        <div>{post.text}</div>
        <div>{post.data}</div>
        <br></br>
      </div>
    )))
}

const Home = () => {
  const serverState = useServer();

  return (
    <div>
      <h1>Your favorite blog</h1>
      <p>Blog list</p>
      <CreatePost serverState={serverState}></CreatePost>
      <ShowPosts serverState={serverState}></ShowPosts>
    </div>
  );
};

export default Home; 