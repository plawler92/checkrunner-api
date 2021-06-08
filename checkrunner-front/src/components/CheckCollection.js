import React from "react";

const CheckCollection = ({ collectionName, collectionType }) => {
  const check_obj = {
    collectionName: collectionName,
    collectionType: collectionType,
  }

  const getRunUrl = (check_obj) => {
    return `http://localhost:5000/api/check?${check_obj.collectionType}=${check_obj.collectionName}`;
  };

  const runCollection = (check_obj) => {
    console.log(check_obj);
    const url = getRunUrl(check_obj);
    console.log(url)
    const data = fetch(url)
      .then((res) => res.json())
      .then((res) => res.check_suite);
    console.log(data);
    return data;
  };

  return (
    <div>
      <h1>{collectionName}</h1>
      <h6>{collectionType}</h6>
      {/* <ul>
        {checks.map((check) => (
          <li key={check}>{check}</li>
        ))}
      </ul> */}
      <button onClick={() => runCollection(check_obj)}>Run</button>
    </div>
  );
};

export default CheckCollection;
