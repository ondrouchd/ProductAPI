using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ProductAPI.Models
{
    [Table("products")]
    public class Product
    {
        [Key]
        [Column("productid")]
        public int ProductID { get; set; }

        [Column("productname")]
        public string ProductName { get; set; }

        [Column("price")]
        public decimal Price { get; set; }

        [Column("category")]
        public string Category { get; set; }
    }
}
