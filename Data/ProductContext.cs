using Microsoft.EntityFrameworkCore;
using ProductAPI.Models;
using System.ComponentModel.DataAnnotations.Schema;

namespace ProductAPI.Data
{
    
    public class ProductContext : DbContext
    {
        public ProductContext(DbContextOptions<ProductContext> options) : base(options)
        {
            
        }
              
        public DbSet<Product> Products { get; set; }
    }
}
