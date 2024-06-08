# Connecting .NET API to PostgreSQL Database
This is a simple example of how to connect a .NET API to a PostgreSQL database. 

## Configure SSL
You can configure the SSL connection to the database by setting the `SSL Mode` in the connection string. The following are the possible values for the `SSL Mode`:
- `Disable` - No SSL
- `Prefer` - Prefer SSL
- `Require` - Require SSL
- `Verify-CA` - Verify CA
- `Verify-Full` - Verify Full
- `Allow` - Allow SSL
- `True` - True
- `False` - False
- `SSL` - SSL
- `SSL Mode` - SSL Mode
- `Use SSL` - Use SSL

## Configuration for Npgsql
The following is the configuration for the Npgsql package in the `appsettings.json` file:
```json
{
  "ConnectionStrings": {
	"DefaultConnection": "Host=localhost;Port=5432;Username=postgres;Password=postgres;Database=postgres;SSL Mode=Require;"
  }
}
```

If you are using Npgsql driver you must specify the `SSL Mode` in the connection string. The `SSL Mode` is set to `Require` in the above example.
You should also specify Root Certificate in the connection string if you are using `Verify-CA` or `Verify-Full` SSL Mode. The following is an example of how to specify the Root Certificate in the connection string:
```json
{
  "ConnectionStrings": {
	"DefaultConnection": "Host=localhost;Port=5432;Username=postgres;Password=postgres;Database=postgres;SSL Mode=Verify-CA;Trust Server Certificate=true;Root Certificate=/path/to/root.crt;"
  }
}
```

Possible values for `Trust Server Certificate` are `true` and `false`. The default value is `false`.
Possible values for Root Certificate are the path to the root certificate file.

## Npgsql documentation
For more information on the Npgsql package, you can visit the [Npgsql documentation](https://www.npgsql.org/doc/index.html).