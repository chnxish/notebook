import React from 'react';

import Layout from '../components/layout';

import FilterableProductTable from '../components/filterable-product-table';

const FPT = () => {
  return (
    <Layout name="Filterable Product Table">
      <div>
        <FilterableProductTable />
      </div>
    </Layout>
  );
}

export default FPT;
