import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import MaterialTable from 'material-table';
import Button from '@material-ui/core/Button';
import TextareaAutosize from "@material-ui/core/TextareaAutosize";

function SerialDecoder(props) {
  const [textValue, setTextValue]  = useState("");
  const [products, setproducts] = useState([])
  const [showResults, setShowResults] = useState(false)

  const handleSubmit = async (event) => {
    event.preventDefault();
    let formatted = textValue.replace(/\n/g, ",").replace(/\s/g, "").split(",");
    let data = {
      query: `
        query {
          productsFromSerials(serials: ${JSON.stringify(formatted)}){
            serial
            productModel
            modelYear
            monthBuilt
            yearBuilt
            factory
            version
            uniqueId
          }
        }
      `
    }
    await axios({
      method: "post",
      url: "http://localhost:5000/graphql",
      data: data,
      headers: { Authorization: `Bearer ${Cookies.get("accessToken")}` }
    })
    .then((response) => {
      setproducts(response.data.data.productsFromSerials)
    })
    .then(() => {
      setShowResults(true)
    })
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>Serial Numbers:</div>
        <TextareaAutosize
          rowsMin={5}
          placeholder="Put serial numbers here:"
          value={textValue}
          onChange={(event) => setTextValue(event.target.value)}
        />
        <Button variant="contained" color="primary" type="submit">
          Decode!
        </Button>
      </form>
      {showResults ? (
        <MaterialTable
          title="Products"
          columns={[
            { title: "Serial Number", field: "serial", editable: "never" },
            {
              title: "Product Model",
              field: "productModel",
              editable: "never",
            },
            { title: "Model Year", field: "modelYear", editable: "never" },
            {
              title: "Month Manufactured",
              field: "monthBuilt",
              editable: "never",
            },
            {
              title: "Year Manufactured",
              field: "yearBuilt",
              editable: "never",
            },
            { title: "Factory", field: "factory", editable: "never" },
            { title: "Version", field: "version", editable: "never" },
            { title: "Unique ID", field: "uniqueId", editable: "never" },
          ]}
          data={products}
        />
      ) : null}
    </div>
  );
}

export default SerialDecoder
