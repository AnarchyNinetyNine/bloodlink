const NameBlock = (
  { hospitalName, setHospitalName }: { hospitalName: string; setHospitalName: React.Dispatch<React.SetStateAction<string>> }
) => {
    return (
      <div className="flex space-x-4">
        <div className="w-full space-y-4">
          <label htmlFor="hospitalName" className="block text-sm font-medium">Hospital Name</label>
          <input
            id="hospitalName"
            type="text"
            placeholder="Hospital Name"
            value={hospitalName}
            onChange={(e) => setHospitalName(e.target.value)}
            className="w-full p-2 border-2 rounded-md bg-background outline-none focus-within:border-blue-700 border-gray-500 transition"
          />
        </div>
      </div>
    );
  };
  
  export default NameBlock;
  