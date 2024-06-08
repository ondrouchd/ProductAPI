using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Caching.Memory;
using ProductAPI.Data;
using ProductAPI.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDbContext<ProductContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
builder.Services.AddMemoryCache();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGet("/products", async (ProductContext db, int page = 1, int pageSize = 100) => 
{
    // validate input query parameters
    if (page < 1 || pageSize < 1)
    {
        return Results.BadRequest("Invalid page or pageSize");
    }

    // use IMemoryCache to cache the results
    var cache = app.Services.GetRequiredService<IMemoryCache>();
    var cacheKey = $"products_{page}_{pageSize}";
    if (cache.TryGetValue(cacheKey, out IEnumerable<Product> products))
    {
        return Results.Ok(products);
    }
    else 
    {
        products = await db.Products.Skip((page - 1) * pageSize).Take(pageSize).ToListAsync();
        cache.Set(cacheKey, products, TimeSpan.FromMinutes(5));
        return Results.Ok(products);
    }
})
.WithName("GetProducts")
.WithDescription("Get a list of products")
.WithMetadata(new { page = 1, pageSize = 100 })
.WithTags("Products")
.WithSummary("Get a list of products")
.WithOpenApi();

app.Run();



