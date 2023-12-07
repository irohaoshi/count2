const shadow = {
  boxShadow: '0 0 20px 20px #eaeaea',
  padding: 40, 
};

const { useState } = React;

const Counter = () => {
  const [count, setCount] = useState(0);
  
  return (
    <div className="container" style={shadow}>
      {console.log('render', count)}
            <div
        className="chevron chevron-up"
         style={{
    visibility: count >= 1000 && 'hidden',
  }}
        onClick={() => {
          setCount(count + 10);
        }}
      />
      <div
        className="chevron chevron-up"
         style={{
    visibility: count >= 1000 && 'hidden',
  }}
        onClick={() => {
          setCount(count + 1);
        }}
      />
      <div className="number">{count}</div>
      <div
        className="chevron chevron-down"
                  style={{
    visibility: count <= 0 && 'hidden',
  }}
        onClick={() => {
          setCount(count - 1);
        }}
      />
      <div className="chevron chevron-down"
          style={{
    visibility: count <= 0 && 'hidden',
  }}
        onClick={() => {
         setCount(count - count);
        }}
      />
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('rat'));
root.render(<Counter />);
